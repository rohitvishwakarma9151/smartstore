import { useEffect, useState } from "react";
import axios from "axios";


function ProductList() {
    const [data, setData] = useState([]);

    useEffect(() => {
    axios.get("http://127.0.0.1:8000/api/products/")
      .then(res => setData(res.data));
  }, []);


  return (
    <div className="conatiner">
        <h2>Furniture & Electronics</h2>
        <div className="row">
            {data.map(product => 
                <div className="col-4" key={product.id}>
                    <div className="card">
                        <img src={`http://127.0.0.1:8000${product.image}`} className="card-img-top"/>
                        <div className="card-body">
                            <h5>{product.name}</h5>
                            <p>₹{product.price}</p>
                            <button className="btn btn-primary">Add to Cart</button>
                        </div>
                    </div>
                </div>
            )}
        </div>
    </div>
  )

}

export default ProductList;