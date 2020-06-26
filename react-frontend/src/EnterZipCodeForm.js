import React from 'react';

export const EnterZipCodeForm = () => {
    return <div className="App">
        <header className="App-header">
            <p>Enter a zip code</p>
            <form action="/<zip_code>" method="get">
                <input type="number" id="name" name="zip code" required
                       minLength="5" maxLength="5" placeholder="Zip Code"></input>
                <input type="submit" value="Submit"></input>
            </form>

        </header>
    </div>
}