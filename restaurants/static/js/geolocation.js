document.getElementById('get-location-btn').onclick = function() {
    // Geolocation APIを使用して現在地を取得
    navigator.geolocation.getCurrentPosition(successCallback, errorCallback);
    alert('位置情報を取得しています。');
}

function successCallback(position){
    console.log(position.coords.latitude);
    console.log(position.coords.longitude);

    alert('緯度: ' + position.coords.latitude + '\n経度: ' + position.coords.longitude);
    var latitude = position.coords.latitude;
    document.getElementById('latitude').value = latitude;

    var longitude = position.coords.longitude;
    document.getElementById('longitude').value = longitude;
}

function errorCallback(error){
    alert('位置情報の取得に失敗しました。');
}