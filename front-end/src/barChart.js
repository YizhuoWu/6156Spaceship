import React, { Component } from 'react';
import Chartkick, { BarChart, LineChart, Timeline, ColumnChart, AreaChart } from 'react-chartkick';
import 'chartkick/chart.js'
import './styles/barChart.css';
// import 'chart.js'

Chartkick.options = {
    colors: ["#00274C", "#FFCB05"]
}

export default class ViewFreqChart extends Component {
	render() {
        console.log("localStorage: ", localStorage.getItem("views"));
        let options = [];
        // if (localStorage.getItem("views") === 'undefined' || localStorage.getItem("views") === null) {

        // } else {

        // let newUserViews = JSON.parse(localStorage.getItem("views"));
        // // Create items array
        // let items = Object.keys(newUserViews).map(function(key) {
        //     return [key, newUserViews[key]];
        // });

        let items = new Object();
        items['business'] = 2;
        items['technology'] = 10;
        items['science'] = 1;
        items['entertainment'] = 1;
        items['general'] = 8;
        items['sports'] = 9;
        items['health'] = 6;

        // Sort the array based on the second element
        // items.sort(function(first, second) {
        //     return second[1] - first[1];
        // });

        Object.keys(items).forEach((label) => {
            options.push([label, items[label]]);
        });

        console.log("options: ", options);
            
        // }

        return (
            <div class="barChart">
                <BarChart data={options} height={500} />
                {/* <BarChart data={[['x', 5], ['y', 10]]} height={500} /> */}
            </div>
        );
	}
}

// export default ViewFreqChart;