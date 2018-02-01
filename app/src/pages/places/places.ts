import { Component } from '@angular/core';
import { NavController } from 'ionic-angular';
import { PlacePage } from '../place/place';

@Component({
  selector: 'page-places',
  templateUrl: 'places.html'
})
export class PlacesPage {
  places = [];
  constructor(public navCtrl: NavController) {
    this.places = [
                   {id:1, events: [{id:1, place_id:1, place_name:"moku", name:'moku-event', date:'moku-event-date', 
                    url:'moku-event-url'}], name:'Möku', address:'Magasini 5, 51005 Tartu', 
                    url:'https://scontent-arn2-1.xx.fbcdn.net/v/t1.0-9/11351304_10153071979438005_8045501394681440696_n.png?oh=b96c3a49314a2febe230f063e31708a8&oe=5AE63CEE'},
                   {id:2, events:[{id:2, place_id:1, place_name:"Sooters", name:'Sooters-event', date:'Sooters-event-date', 
                    url:'Shooters-event-url'}], name:'Shooters Tartu', address:'Vallikraavi 4, 51003 Tartu', 
                    url:'https://scontent-arn2-1.xx.fbcdn.net/v/t1.0-9/10628334_804973896200970_4372812118889677304_n.png?oh=a3149f470f65df135af126aa52d67016&oe=5B164B95'},
                   {id:3, events:[{id:3, place_id:1, place_name:"Illusion", name:'Illusion-event', date:'Illusion-event-date', 
                    url:'Illusion-event-url'}], name:'Club Illusion', address:'Raatuse 97, 50604 Tartu', 
                    url:'https://scontent-arn2-1.xx.fbcdn.net/v/t1.0-9/12814752_10154622559082586_7774026446257800171_n.png?oh=98e93e011019a39aeb9c24d7e72e7338&oe=5B2628AE'}
                  ];
  }

  openPlacePage(place) {
    this.navCtrl.push(PlacePage, { place: place});
  }

}



