async function get_crypto_price(crypto, currency) {
    const url = `https://api.coingecko.com/api/v3/simple/price?ids=${crypto}&vs_currencies=${currency}`;
    const response = await fetch(url);
    const data = await response.json();
    console.log(data);
    return data[crypto][currency];
}

async function convert_crypto_to_fiat(amount, crypto, fiat_currency) {
    const price = await get_crypto_price(crypto, fiat_currency);
    if (price) {
        return amount * price;
    } else {
        return null;
    }
}

// Definindo os parâmetros
const amount_of_crypto = 1;
var crypto_currency = "bitcoin";
var fiat_currency = "brl";

// Convertendo
convert_crypto_to_fiat(amount_of_crypto, crypto_currency, fiat_currency)
    .then(result => {
        if (result !== null) {
            console.log(`${amount_of_crypto} ${crypto_currency.toUpperCase()} equivale a ${result} ${fiat_currency.toUpperCase()}`);
        } else {
            console.log("Não foi possível obter o preço. Verifique sua entrada ou tente novamente mais tarde.");
        }
    })
    .catch(error => {
        console.error("Ocorreu um erro:", error);
    });

async function get_crypto_price(crypto, currency) {
    const url = `https://api.coingecko.com/api/v3/simple/price?ids=${crypto}&vs_currencies=${currency}`;
    const response = await fetch(url);
    const data = await response.json();
    return data[crypto][currency];
}

async function convert_fiat_to_crypto(amount, fiat_currency, crypto_currency) {
    const price = await get_crypto_price(crypto_currency, fiat_currency);
    if (price) {
        console.log(amount, price)
        return amount / price;
    } else {
        return null;
    }
}

// Definindo os parâmetros
const amount_of_fiat = 1; // por exemplo, 100 dólares
var crypto_currency = "bitcoin";
var fiat_currency = "brl";

// Convertendo
convert_fiat_to_crypto(amount_of_fiat, fiat_currency, crypto_currency)
    .then(result => {
        if (result !== null) {
            console.log(`${amount_of_fiat} ${fiat_currency.toUpperCase()} equivale a ${result} ${crypto_currency.toUpperCase()}`);
        } else {
            console.log("Não foi possível obter o preço. Verifique sua entrada ou tente novamente mais tarde.");
        }
    })
    .catch(error => {
        console.error("Ocorreu um erro:", error);
    });
