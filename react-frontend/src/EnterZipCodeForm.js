import React from 'react';
import { Form, Input, Button } from "semantic-ui-react";

export default class EnterZipCodeForm extends React.Component {
    constructor(props) {
        super(props);
        this.state = { value: '' }

        this.handleChange = this.handleChange.bind(this);
        this.handleSubmit = this.handleSubmit.bind(this);
    }

    //Set the value state as things are entered into the box
    handleChange(event) {
        this.setState({value: event.target.value})
    }

    //When submitted, call the fetchData function from parent and pass it the inputted value
    handleSubmit() {
        this.props.fetchData(this.state.value);
    }

    render() {
        return (
            <div>
                <Form>
                        <Input
                            placeholder="Zip Code"
                            onChange={this.handleChange}
                            onSubmit={this.handleSubmit}
                        />
                </Form>
                <Form>
                    <Button onClick={this.handleSubmit}>
                            Submit
                        </Button>
                </Form>
            </div>
        );
    }
}