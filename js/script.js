/* window.onload = function() {
    var gauges = document.querySelectorAll('.gauge');

    console.log('Anzahl der Gauge-Elemente: ' + gauges.length);

    gauges.forEach(function(gaugeElement) {
        var value = parseFloat(gaugeElement.dataset.value);
        var threshold = parseFloat(gaugeElement.dataset.threshold);

        console.log('Wert: ' + value);
        console.log('Schwellwert: ' + threshold);

        var gauge = new Gauge(gaugeElement, {
            angle: 0.5,
            lineWidth: 0.1,
            radiusScale: 0.9,
            pointer: {
                length: 0.8,
                strokeWidth: 0.03,
                color: '#000000'
            },
            staticLabels: {
                font: '10px sans-serif',
                labels: [0, threshold, threshold * 2],
                color: '#000000',
                fractionDigits: 0
            },
            staticZones: [
               {stroke: '#FF0000', from: 0, to: 50}, // Rot
               {stroke: '#00FF00', from: 50, to: 100}  // Grün
            ],
            limitMax: true,
            limitMin: true,
            highDpiSupport: true
        });
        gauge.maxValue = threshold * 2;
        gauge.set(value);
    });
}; */

