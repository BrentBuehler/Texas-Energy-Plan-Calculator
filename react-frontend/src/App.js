import React, { Component } from 'react';
import './App.css';
import ListPlanResults from './ListPlanResults.js'
import EnterZipCodeForm from './EnterZipCodeForm.js'

class App extends Component {
    constructor(props) {
        super(props);
        this.state = {
            zipCode: '',
            plans: [],
            isLoaded: false,
            error: null
        }
        this.fetchData = this.fetchData.bind(this);
    }

    //Call this function when a zip code is searched
    fetchData(zip) {
        //If the searched zip is the same as the one already searched, don't search again:
        if (this.state.zipCode == zip) {
            return;
        } else {
            //Otherwise, get the data from the server and set the result to "plans"
            this.setState({zipCode: zip})
            fetch('/zip_code/' + zip)
                .then(res => res.json())
                .then(
                    (result) => {
                        this.setState({
                            isLoaded: true,
                            plans: result
                        });
                    },
                    (error) => {
                        this.setState({
                            isLoaded: true,
                            error
                        });
                    }
                )
        }
    }

    render() {
        //Don't render the list if there is no data available to pass to it:
        let plans = (this.state.plans === []) ?
            null :
            <ListPlanResults plans={this.state.plans}/>

        //Render the EnterZipCodeForm and pass it the fetchData function
        return (
            <div className="App">
                <EnterZipCodeForm fetchData={this.fetchData} />
                {plans}
            </div>
        )
    }
}

export default App;