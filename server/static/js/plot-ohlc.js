function plot_ohlc() {
    'use strict';

    var trace = {
        type:       "ohlc",
        xaxis:      "x",
        yaxis:      "y",
        x:          dates,
        open:       d_o,
        high:       d_h,
        low:        d_c,
        close:      d_l,
        line:       {color: 'rgba(31,119,180,1)'},
        increasing: {line: {color: '#17BECF'}},
        decreasing: {line: {color: '#7F7F7F'}},
    }

    var data = [trace];

    var layout = {
        margin: {
            l: 50, r: 50,
            b: 50, t: 50,
            pad: 0
        },
        showlegend: false,
        xaxis: {
            autorange: true,
            type: 'date'
        },
        yaxis: {
            autorange: true,
            type: 'linear'
        }
    };

    Plotly.plot('plot-ohlc', data, layout);
};

plot_ohlc();
