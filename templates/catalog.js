import React, { useEffect } from "react";


export default function() {

  useEffect(() =>{fetch("http://localhost:5000/product")})

  return (
    <div>
      <div class="header">
        <h1>Droids For Sale:</h1>
      </div>
      <div class="catalog_body">
        <table>
          <tr>
            <td>Model Image</td>
            <td>Model</td>
            <td>Price(USD)</td>
            <td>Description</td>
          </tr>
          <tr>
            <td id ="b1"></td>
            <td>{{productName1}}</td>
            <td>&#36;{{price1}}</td>
            <td>{{description1}}</td>
          </tr>
          <tr>
            <td id="b2"></td>
            <td>{{productName2}}</td>
            <td>&#36;{{price2}}</td>
            <td>{{description2}}</td>
          </tr>
          <tr>
            <td id="Droideka"></td>
            <td>{{productName3}}</td>
            <td>&#36;{{price3}}</td>
            <td>{{description3}}</td>
          </tr>
        </table>
      </div>
    </div>
  );
}