function plot_candle() {
    'use strict';

    var trace = {
        type:       "candlestick",
        xaxis:      "x",
        yaxis:      "y",
        x:          dates,
        open:       d_o,
        high:       d_h,
        low:        d_l,
        close:      d_c,
        line:       {color: 'rgba(31,119,180,1)'},
        increasing: {line: {color: '#17BECF'}},
        decreasing: {line: {color: '#7F7F7F'}},
    }

    var data = [trace];

    var layout = {
        margin: margin,
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

    Plotly.plot('plot-candle', data, layout);
};

plot_candle();
