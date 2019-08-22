import React, { Component } from "react";

class ItemList extends Component {
  constructor(props) {
    super(props);
  }

  render() {
    console.log(this.props.items);
    return (
      <div>
        <div>
          {this.props.items.map((el) => {
            return <Item id={el} />;
          })}
        </div>
      </div>
    );
  }
}

class Item extends Component {
  constructor(props) {
    super(props);
    this.state = {
      loading: true
    };
  }
  componentDidMount() {
    fetch("/item/get/" + this.props.id)
      .then((res) => res.json())
      .then((data) => {
        console.log(data);
        this.setState({ item: data, loading: false });
      });
  }

  render() {
    let temp;
    if (this.state.loading) {
      temp = (
        <div>
          <h1>Loading</h1>
        </div>
      );
    } else {
      temp = (
        <div className='item-grid'>
          <div>
            <p>Name: {this.state.item.name}</p>
          </div>
          <div>
            <p>Art Nr: {this.state.item.item.articleNumber}</p>
          </div>
          <div>
            <p>Price: {this.state.item.item.sellPrice}</p>
          </div>
          <div>
            <p>Inventory: {this.state.item.item.inventory}</p>
          </div>
        </div>
      );
    }
    return (
      <div className='w3-border'>
        <h1>{temp}</h1>
      </div>
    );
  }
}

export default ItemList;
