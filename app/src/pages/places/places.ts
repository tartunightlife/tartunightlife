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
                    url:'moku-event-url'}], name:'moku', address:'moku-address', url:'moku-url'},
                   {id:2, events:[{id:2, place_id:1, place_name:"Sooters", name:'Sooters-event', date:'Sooters-event-date', 
                    url:'Sooters-event-url'}], name:'Sooters', address:'Sooters-address', url:'Sooters-url'},
                   {id:3, events:[{id:3, place_id:1, place_name:"Illusion", name:'Illusion-event', date:'Illusion-event-date', 
                    url:'Illusion-event-url'}],name:'Illusion', address:'Illusion-address', url:'Illusion-url'}
                  ];
  }

  openPlacePage(place) {
    this.navCtrl.push(PlacePage, { place: place});
  }

}



