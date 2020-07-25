import React from 'react';
import {List, Header} from 'semantic-ui-react';

export default function ListPlanResults(props) {

    //Maps over and makes a list of the plans from props:
    return (
        <List>
            {props.plans.map(plan => {
                return (
                    <List.Item key={plan.id}>
                        <Header>{plan.id} plan name: {plan.plan_name}</Header>
                    </List.Item>
                );
            })}
        </List>
    );
}
