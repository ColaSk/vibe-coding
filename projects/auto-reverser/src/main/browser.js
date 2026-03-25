const puppeteer = require('puppeteer');

class BrowserController {
    constructor() {
        this.browser = null;
        this.page = null;
        this.pages = new Map();
    }

    async launch(url, options = {}) {
        const defaultOptions = {
            headless: false,
            devtools: true,
            args: [
                '--auto-open-devtools-for-tabs',
                '--disable-features=IsolateOrigins,site-per-process',
                '--no-sandbox',
                '--disable-setuid-sandbox',
                '--disable-dev-shm-usage',
                '--disable-accelerated-2d-canvas',
                '--no-first-run',
                '--no-zygote',
                '--disable-gpu'
            ]
        };

        const launchOptions = { ...defaultOptions, ...options };
        
        this.browser = await puppeteer.launch(launchOptions);
        this.page = await this.browser.newPage();

        await this.setupPage(this.page);

        this.pages.set(this.page.mainFrame().id, this.page);

        return this.page;
    }

    async setupPage(page) {
        await page.setUserAgent(
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) ' +
            'AppleWebKit/537.36 (KHTML, like Gecko) ' +
            'Chrome/119.0.0.0 Safari/537.36'
        );

        await page.setViewport({ width: 1920, height: 1080 });

        await page.setRequestInterception(true);

        await this.injectAntiAntiDebug(page);
    }

    async injectAntiAntiDebug(page) {
        await page.evaluateOnNewDocument(() => {
            const originalDebugger = Object.getOwnPropertyDescriptor(
                Window.prototype, 'debugger'
            );

            Object.defineProperty(Window.prototype, 'debugger', {
                get: function() { return undefined; },
                set: function() {}
            });

            const originalConsole = window.console;
            Object.defineProperty(window, 'console', {
                get: function() { return originalConsole; },
                set: function() {}
            });

            const originalToString = Function.prototype.toString;
            Function.prototype.toString = function() {
                if (this === originalDebugger?.get) {
                    return 'function getter() { [native code] }';
                }
                return originalToString.call(this);
            };

            const originalDefineProperty = Object.defineProperty;
            Object.defineProperty = function(obj, prop, descriptor) {
                if (prop === 'debugger') {
                    return obj;
                }
                return originalDefineProperty.call(this, obj, prop, descriptor);
            };
        });
    }

    async navigate(url) {
        if (!this.page) {
            throw new Error('Page not initialized');
        }
        
        await this.page.goto(url, { 
            waitUntil: 'networkidle2',
            timeout: 60000 
        });
    }

    async waitForNavigation(timeout = 30000) {
        if (!this.page) return;
        
        await this.page.waitForNavigation({
            waitUntil: 'networkidle2',
            timeout: timeout
        });
    }

    async executeScript(script) {
        if (!this.page) {
            throw new Error('Page not initialized');
        }
        
        return await this.page.evaluate(script);
    }

    async getCookies() {
        if (!this.page) return [];
        return await this.page.cookies();
    }

    async setCookies(cookies) {
        if (!this.page) return;
        await this.page.setCookie(...cookies);
    }

    async getLocalStorage() {
        if (!this.page) return {};
        return await this.page.evaluate(() => {
            const items = {};
            for (let i = 0; i < localStorage.length; i++) {
                const key = localStorage.key(i);
                items[key] = localStorage.getItem(key);
            }
            return items;
        });
    }

    async getScripts() {
        if (!this.page) return [];
        
        return await this.page.evaluate(() => {
            return Array.from(document.querySelectorAll('script[src]'))
                .map(s => s.src);
        });
    }

    async fetchScript(url) {
        if (!this.page) return null;
        
        const response = await this.page.goto(url);
        return await response.text();
    }

    async autoScroll() {
        if (!this.page) return;
        
        await this.page.evaluate(async () => {
            await new Promise((resolve) => {
                let totalHeight = 0;
                const distance = 100;
                const timer = setInterval(() => {
                    const scrollHeight = document.body.scrollHeight;
                    window.scrollBy(0, distance);
                    totalHeight += distance;

                    if (totalHeight >= scrollHeight - window.innerHeight) {
                        clearInterval(timer);
                        resolve();
                    }
                }, 100);
            });
        });
    }

    async close() {
        if (this.browser) {
            await this.browser.close();
            this.browser = null;
            this.page = null;
            this.pages.clear();
        }
    }

    getPage() {
        return this.page;
    }

    getBrowser() {
        return this.browser;
    }
}

module.exports = { BrowserController };
