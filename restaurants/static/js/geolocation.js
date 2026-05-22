document.getElementById('get-location-btn').onclick = function() {
    // Geolocation APIを使用して現在地を取得
    navigator.geolocation.getCurrentPosition(successCallback, errorCallback);
    alert('位置情報を取得しています。');
}

function successCallback(position){

    alert('位置情報を取得しました。');
    var latitude = position.coords.latitude;
    document.getElementById('latitude').innerHTML = latitude;

    var longitude = position.coords.longitude;
    document.getElementById('longitude').innerHTML = longitude;
}

function errorCallback(error){
    alert('位置情報の取得に失敗しました。');
}