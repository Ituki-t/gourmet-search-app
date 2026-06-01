
function successCallback(position){
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

const rangeElement = document.getElementById('range');
rangeElement.addEventListener('change', function() {
    sessionStorage.setItem('range', rangeElement.value);
})

window.addEventListener('load', function() {
    const lat = sessionStorage.getItem('lat');
    const lng = sessionStorage.getItem('lng');
    const range = sessionStorage.getItem('range');

    if (lat && lng) {
        document.getElementById('latitude').value = lat;
        document.getElementById('longitude').value = lng;
    } else {
        // Geolocation APIを使用して現在地を取得
        navigator.geolocation.getCurrentPosition(successCallback, errorCallback);
    }

    setInterval(() => {
        navigator.geolocation.getCurrentPosition(successCallback, errorCallback);
    }, 60000); // 1分ごとに位置情報を更新

    if (range) {
        document.getElementById('range').value = range;
    }
})

