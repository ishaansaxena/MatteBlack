var data = [
  {
    x: ['2013-10-04 22:23:00', '2013-11-04 22:23:00', '2013-12-04 22:23:00'],
    y: [1, 3, 6],
    type: 'scatter'
  }
];

var layout = {
  margin: {
    l: 10,
    r: 10,
    b: 40,
    t: 40,
    pad: 0
  }
};

Plotly.newPlot('plot-main', data, layout);
