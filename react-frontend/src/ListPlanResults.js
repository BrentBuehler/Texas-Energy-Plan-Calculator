import React from 'react';
import {List, Header, Card, Grid} from 'semantic-ui-react';

export default function ListPlanResults(props) {

    //Maps over and makes a list of the plans from props:
    return (
            <List>
                {props.plans.map(plan => {
                    return (
                        <Grid centered={2}>
                            <List.Item>
                                <Card key={plan.plan_id}>
                                    <Card.Header>{plan.plan_name}</Card.Header>
                                    <Header>{plan.plan_id} plan name: {plan.plan_name}</Header>
                                </Card>
                            </List.Item>
                        </Grid>
                    );
                })}
            </List>
    );
}
