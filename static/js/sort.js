function sortByView(id1,id2) {

    document.getElementsByID(id1).innerHTML = "{{ view.0.name }}<br>{{ view.0.description }}";
    document.getElementsByID(id2).innerHTML = "{{ view.1.name }}<br>{{ view.1.description }}";
 }

function sortByQuality(id1,id2) {
    document.getElementsByID(id1).innerHTML = "{{ qual.1.name }}<br>{{ qual.0.description }}";
    document.getElementsByID(id2).innerHTML = "{{ qual.1.name }}<br>{{ qual.1.description }}";
}

function sortByMusic(id1,id2) {
    document.getElementsByID(id1).innerHTML = "{{ musi.0.name }}<br>{{ musi.0.description }}";
    document.getElementsByID(id2).innerHTML = "{{ musi.1.name }}<br>{{ musi.1.description }}";
}

function sortByCommunity(id1,id2) {
    document.getElementsByID(id1).innerHTML = "{{ comm.0.name }}<br>{{ comm.0.description }}";
    document.getElementsByID(id2).innerHTML = "{{ comm.1.name }}<br>{{ comm.1.description }}";
 }

function upPage(id1,id2){
    document.getElementsByID(id1).innerHTML = "{{ view.0.name }}<br>{{ view.0.description }}";
    document.getElementsByID(id2).innerHTML = "{{ view.1.name }}<br>{{ view.1.description }}";
}

function downPage(id1,id2){
    document.getElementsByID(id1).innerHTML = "{{ view.1.name }}<br>{{ view.1.description }}";
    document.getElementsByID(id2).innerHTML = "{{ view.2.name }}<br>{{ view.2.description }}";
}
 