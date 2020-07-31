function getCount(objects) {
    for (let p in objects) {
        return objects.filter(item => item.x == item.y).length;
    }
}
