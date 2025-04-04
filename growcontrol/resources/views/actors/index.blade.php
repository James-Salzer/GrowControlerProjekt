<!DOCTYPE html>
<html>
<head>
    <title>Aktoren</title>
</head>
<body>
    <h1>Aktoren</h1>
    <table>
        <thead>
            <tr>
                <th>Name</th>
                <th>Zustand</th>
            </tr>
        </thead>
        <tbody>
            @foreach ($actors as $actor)
                <tr>
                    <td>{{ $actor->actor_name }}</td>
                    <td>{{ $actor->is_on }}</td>
                </tr>
            @endforeach
        </tbody>
    </table>
</body>
</html>