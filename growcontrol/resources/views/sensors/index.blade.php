<!DOCTYPE html>
<html>
<head>
    <title>Sensoren</title>
</head>
<body>
    <h1>Sensoren</h1>
    <table>
        <thead>
            <tr>
                <th>Name</th>
                <th>Wert</th>
                <th>Art</th>
                <th>Schwellwert</th>
                <th>Diagramm</th>
            </tr>
        </thead>
        <tbody>
            @foreach ($sensors as $sensor)
                <tr>
                    <td>{{ $sensor->sensor_name }}</td>
                    <td></td>
                    <td></td>
                    <td></td>
                    <td></td>
                </tr>
            @endforeach
        </tbody>
    </table>
</body>
</html>