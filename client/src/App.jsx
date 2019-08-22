import React, { Component } from "react";
import ItemList from "./components/Items.jsx";

export default class App extends Component {
  constructor(props) {
    super(props);
    this.state = {
      loading: true,
      items: []
    };
  }

  componentDidMount() {
    fetch("/item/list")
      .then((res) => res.json())
      .then((data) => {
        //console.log(data);
        this.setState({ loading: false, items: data });
      });
  }

  render() {
    var itemList;
    if (this.state.loading) {
      itemList = <h1>Loading Application</h1>;
    } else {
      itemList = <ItemList items={this.state.items} />;
    }
    return <div>{itemList}</div>;
  }
}
