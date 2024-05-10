// RECOMENDO O ATALHO (CTRL + END) PARA IR AO FINAL DO SCRIPT
const dataFiat = [
    {
        "name": "United States Dollar",
        "code": "USD",
        "country": "United States"
    },
    {
        "name": "Euro",
        "code": "EUR",
        "country": "Eurozone"
    },
    {
        "name": "Japanese Yen",
        "code": "JPY",
        "country": "Japan"
    },
    {
        "name": "British Pound Sterling",
        "code": "GBP",
        "country": "United Kingdom"
    },
    {
        "name": "Australian Dollar",
        "code": "AUD",
        "country": "Australia"
    },
    {
        "name": "Canadian Dollar",
        "code": "CAD",
        "country": "Canada"
    },
    {
        "name": "Swiss Franc",
        "code": "CHF",
        "country": "Switzerland"
    },
    {
        "name": "Hong Kong Dollar",
        "code": "HKD",
        "country": "Hong Kong"
    },
    {
        "name": "Swedish Krona",
        "code": "SEK",
        "country": "Sweden"
    },
    {
        "name": "New Zealand Dollar",
        "code": "NZD",
        "country": "New Zealand"
    },
    {
        "name": "Norwegian Krone",
        "code": "NOK",
        "country": "Norway"
    },
    {
        "name": "Mexican Peso",
        "code": "MXN",
        "country": "Mexico"
    },
    {
        "name": "Singapore Dollar",
        "code": "SGD",
        "country": "Singapore"
    },
    {
        "name": "South Korean Won",
        "code": "KRW",
        "country": "South Korea"
    },
    {
        "name": "Russian Ruble",
        "code": "RUB",
        "country": "Russia"
    },
    {
        "name": "Danish Krone",
        "code": "DKK",
        "country": "Denmark"
    },
    {
        "name": "Turkish Lira",
        "code": "TRY",
        "country": "Turkey"
    },
    {
        "name": "South African Rand",
        "code": "ZAR",
        "country": "South Africa"
    },
    {
        "name": "New Taiwan Dollar",
        "code": "TWD",
        "country": "Taiwan"
    },
    {
        "name": "Brazilian Real",
        "code": "BRL",
        "country": "Brazil"
    },
    {
        "name": "Indian Rupee",
        "code": "INR",
        "country": "India"
    },
    {
        "name": "Hong Kong Dollar",
        "code": "HKD",
        "country": "Hong Kong"
    },
    {
        "name": "Philippine Peso",
        "code": "PHP",
        "country": "Philippines"
    },
    {
        "name": "Thai Baht",
        "code": "THB",
        "country": "Thailand"
    },
    {
        "name": "Czech Koruna",
        "code": "CZK",
        "country": "Czech Republic"
    },
    {
        "name": "Chinese Yuan Renminbi",
        "code": "CNY",
        "country": "China"
    },
    {
        "name": "Polish Zloty",
        "code": "PLN",
        "country": "Poland"
    },
    {
        "name": "Israeli New Shekel",
        "code": "ILS",
        "country": "Israel"
    },
    {
        "name": "United Arab Emirates Dirham",
        "code": "AED",
        "country": "United Arab Emirates"
    },
    {
        "name": "Icelandic Krona",
        "code": "ISK",
        "country": "Iceland"
    },
    {
        "name": "Chilean Peso",
        "code": "CLP",
        "country": "Chile"
    },
    {
        "name": "Malaysian Ringgit",
        "code": "MYR",
        "country": "Malaysia"
    },
    {
        "name": "Barbados Dollar",
        "code": "BBD",
        "country": "Barbados"
    },
    {
        "name": "Hungarian Forint",
        "code": "HUF",
        "country": "Hungary"
    },
    {
        "name": "Cayman Islands Dollar",
        "code": "KYD",
        "country": "Cayman Islands"
    },
    {
        "name": "Trinidad and Tobago Dollar",
        "code": "TTD",
        "country": "Trinidad and Tobago"
    },
    {
        "name": "Suriname Dollar",
        "code": "SRD",
        "country": "Suriname"
    },
    {
        "name": "Bulgarian Lev",
        "code": "BGN",
        "country": "Bulgaria"
    },
    {
        "name": "Lebanese Pound",
        "code": "LBP",
        "country": "Lebanon"
    },
    {
        "name": "Saudi Riyal",
        "code": "SAR",
        "country": "Saudi Arabia"
    },
    {
        "name": "Colombian Peso",
        "code": "COP",
        "country": "Colombia"
    },
    {
        "name": "Fiji Dollar",
        "code": "FJD",
        "country": "Fiji"
    },
    {
        "name": "Belize Dollar",
        "code": "BZD",
        "country": "Belize"
    },
    {
        "name": "Argentine Peso",
        "code": "ARS",
        "country": "Argentina"
    },
    {
        "name": "Bermuda Dollar",
        "code": "BMD",
        "country": "Bermuda"
    },
    {
        "name": "Brunei Dollar",
        "code": "BND",
        "country": "Brunei"
    }
]; // lenght: 50

class CryptoContainerSearch {
    constructor(fiatData) {
        this.inputSearch = document.querySelector("[data-search]");
        this.currentCurrency = document.querySelector("[data-currency]");
        this.cryptoList = document.querySelector("[data-crypto-list]");
        this.cryptoDetailsDiv = document.querySelector("[data-crypto-details]")
        this.listCoins = null;
        this.switchKey = false;
        this.fiatList = fiatData;
        this.fiatListContainer = document.querySelector("[data-fiat-list]");
        this.trade = {
            currentPrice: null,
            currentCurrency: null,
            currentCrypto: null,
        }
        this.inputsTrade = {
            entry: document.querySelector("[data-screen1]"),
            output: document.querySelector("[data-screen2]"),
            currencyEntry: document.querySelector("[data-screen3]"),
            currencyOutput: document.querySelector("[data-screen4]"),
        }
    }
    async getCryptoList(currencyCode) {
        try {
            const request = await fetch(`https://api.coingecko.com/api/v3/coins/markets?vs_currency=${currencyCode}&order=market_cap_desc&per_page=200&page=1&sparkline=false`)
            const response = await request.json();
            const newData = response.map((cryptoData) => {  
                return {
                    id: cryptoData.id,
                    symbol: cryptoData.symbol,
                    name: cryptoData.name,
                    image: cryptoData.image,
                    currentPrice: cryptoData.current_price,
                    lastUpdate: cryptoData.last_updated,
                    rank: cryptoData.market_cap_rank
                }
            });
            this.listCoins = newData;
            this.loadCardsList(newData);
        } catch (error) {
            console.log(error, error.message)
        }
    }
    createMiniCardComponent(data, currentCurrency) {
        const component = document.createElement('div');
        component.classList.add('mini-card-component')

        component.innerHTML = `
        <div class="crypto-logo">
            <img src="${data.image}" alt="crypto-logo">
        </div>
        <div class="labels">
            <h3 class="title-crypto">${data.name}<span>/${data.symbol}</span></h3>
            <p class="price-crypto"><span>current quote:</span> ${data.currentPrice} ${currentCurrency}</p>
        </div>
        `

        component.addEventListener('click', () => {
            this.cryptoDetailsDiv.innerHTML = ""
            this.cryptoDetailsDiv.append(this.createCardDetails(data, currentCurrency))
            this.addInfosTrade(1, data.currentPrice, data.symbol, currentCurrency)
            this.trade.currentPrice = data.currentPrice;
            this.trade.currentCrypto = data.symbol;
            this.trade.currentCurrency = currentCurrency;
            if(this.switchKey)
                this.switchKey = false;

            const container = document.querySelector("[data-container-convert]");
            container.classList.contains("screen-off") && container.classList.remove("screen-off");

        });

        return component;
    }
    createCardDetails(data, currentCurrency) {
        const component = document.createElement('div');
        component.classList.add('card-details')

        component.innerHTML = `
        <div class="card-logo-label">   
            <img src="${data.image}" alt="logo-crypto">
            <h3 class="title-card">${data.name}<span>/${data.symbol}</span></h3>
        </div>
        <p class="description-card">Lorem ipsum dolor, sit amet consectetur adipisicing elit. Dicta laboriosam ullam, suscipit architecto error ipsum. Molestiae labore harum dolore illum, expedita debitis maiores. Eveniet rem quidem, sunt totam nisi cumque!</p>
        <div class="infos-card">
            <strong class="txt-info">last update: <span>${data.lastUpdate.slice(0, 10)}</span></strong>
            <strong class="txt-info">current quote: <span style="color: green;">${data.currentPrice}</span></strong>
            <strong class="txt-info">in currency: <span>${currentCurrency}</span></strong>
        </div>
        `
        return component;
    }
    createSelectCard(code, name) {
        const selectBox = document.createElement("div");
        selectBox.classList.add("select-fiat");
        selectBox.innerHTML = `
            <span data-fiat-currency>${code}</span>/${name}
        `

        selectBox.addEventListener('mousedown', (e) => {
            const codeFiat = e.target.children[0].innerText
            this.currentCurrency.value = codeFiat;
            this.getCryptoList(codeFiat.toLowerCase());
        });

        return selectBox;
    }

    loadCardsList(dataList) {
        this.cryptoList.innerHTML = ""
        dataList.forEach((cryptoDt) => {
            this.cryptoList.append(this.createMiniCardComponent(
                cryptoDt, this.currentCurrency.value
            ));
        });
    }

    searchAction() {
        this.inputSearch.addEventListener('keyup', (e) => {
            const searchList = this.listCoins.filter(
                (data) => data.name.toLowerCase().includes(e.target.value.toLowerCase()))

            this.cryptoList.innerHTML = ""
            searchList.forEach((data) => {
                this.cryptoList.append(this.createMiniCardComponent(
                    data, this.currentCurrency.value
                ))
            });
        });
    }

    addInfosTrade(amount, currentPrice, cryptoSymbol, currentCurrency) {
        this.inputsTrade.entry.value = amount;
        this.inputsTrade.output.value = currentPrice;
        this.inputsTrade.currencyEntry.value = cryptoSymbol;
        this.inputsTrade.currencyOutput.value = currentCurrency;
    }

    regexS() {
        this.inputsTrade.entry.addEventListener('keydown', (e) => {
            // console.log(e.key)
            if(e.key !== "Backspace")
                e.preventDefault()   

            const regex = /^[0-9.]+$/;
            if(regex.test(e.key))
                this.inputsTrade.entry.value = e.target.value + e.key
        });
        this.currentCurrency.addEventListener('keydown', (e) => {
            const regex = /^[a-zA-Z]{3}$/;
            if(regex.test(e.target.value))
                (e.key !== "Backspace") && e.preventDefault();
        });
    }

    actionGetDataConvert() {
        this.inputsTrade.entry.addEventListener('keyup', () => {
            const number = Number(this.inputsTrade.entry.value);
            if(isNaN(number)){
                console.log('not a number')
                return
            }

            if(!this.switchKey) {
                // const outputFormated = this.inputsTrade.output.value.replace(/\./g, '').replace(/,/g, '.');
                const convert = number * this.trade.currentPrice;
                this.inputsTrade.output.value = convert.toString();
                // .replace(/\B(?=(\d{3})+(?!\d))/g, '.')
            } else {
                const convert = number / this.trade.currentPrice;
                this.inputsTrade.output.value = convert.toString();
            }
            
            return
        });
    }

    actionSwitchConvert() {
        document.querySelector("[data-switch-button]").addEventListener('click', () => {
            if(!this.switchKey) {
                this.inputsTrade.entry.value = this.trade.currentPrice;
                this.inputsTrade.output.value = 1;
                this.inputsTrade.currencyEntry.value = this.trade.currentCurrency;
                this.inputsTrade.currencyOutput.value = this.trade.currentCrypto;
            } else {
                this.inputsTrade.entry.value = 1;
                this.inputsTrade.output.value = this.trade.currentPrice;
                this.inputsTrade.currencyEntry.value = this.trade.currentCrypto;
                this.inputsTrade.currencyOutput.value = this.trade.currentCurrency;
            }
            this.switchKey = !this.switchKey;
        });
    }

    loadFiatList() {
        this.fiatList.forEach((currency) => {
            this.fiatListContainer.append(this.createSelectCard(currency.code, currency.name));
        });
    }
    searchFiatAction() {
        this.currentCurrency.addEventListener('keyup', (e) => {
            const searchList = this.fiatList.filter(
                (data) => data.code.includes(e.target.value.toUpperCase())
            )

            this.fiatListContainer.innerHTML = ""
            searchList.forEach((currency) => {
                this.fiatListContainer.append(this.createSelectCard(currency.code, currency.name));
            });
        });
    }
    openCloseListFiat() {
        this.currentCurrency.addEventListener('focus', () => {
            this.fiatListContainer.classList.remove('screen-off')
        });
        this.currentCurrency.addEventListener('blur', () => {
            this.fiatListContainer.classList.add('screen-off')
        });
    }
}

const main = new CryptoContainerSearch(dataFiat);
main.getCryptoList("brl")
// main.loadCardsList(dataTest);
main.searchAction();
main.regexS();
main.actionGetDataConvert();
main.actionSwitchConvert();
main.loadFiatList();
main.searchFiatAction();
main.openCloseListFiat();