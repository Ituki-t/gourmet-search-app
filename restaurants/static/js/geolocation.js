
// Geolocation APIを使用して現在地を取得
navigator.geolocation.getCurrentPosition(successCallback, errorCallback);


function successCallback(position){
    console.log('緯度: ' + position.coords.latitude, '経度: ' + position.coords.longitude);

    // alert('緯度: ' + position.coords.latitude + '\n経度: ' + position.coords.longitude);
    const latitude = position.coords.latitude;
    document.getElementById('latitude').value = latitude;
    sessionStorage.setItem('lat', latitude);

    const longitude = position.coords.longitude;
    document.getElementById('longitude').value = longitude;
    sessionStorage.setItem('lng', longitude);
}

function errorCallback(error){
    console.error('位置情報の取得に失敗しました。');
}


window.addEventListener('load', function() {
    const lat = sessionStorage.getItem('lat');
    const lng = sessionStorage.getItem('lng');

    if (lat && lng) {
        document.getElementById('latitude').value = lat;
        document.getElementById('longitude').value = lng;
    }
})