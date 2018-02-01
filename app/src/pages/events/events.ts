import { Component } from '@angular/core';
import { NavController } from 'ionic-angular';
import { EventPage } from '../event/event';

@Component({
  selector: 'page-evnts',
  templateUrl: 'events.html'
})
export class EventsPage {
  
  events = [];
  constructor(public navCtrl: NavController) {
    this.events = [
                  {id:1, place_id:1, place_name:"moku", name:'moku-event', date:'moku-event-date', url:'moku-event-url'},
                  {id:2, place_id:1, place_name:"Sooters", name:'Sooters-event', date:'Sooters-event-date', url:'Sooters-event-url'},
                  {id:3, place_id:1, place_name:"Illusion", name:'Illusion-event', date:'Illusion-event-date', url:'Illusion-event-url'}
                  ];
  }


  openEventPage(event) {
    this.navCtrl.push(EventPage, { event: event});
  }
}
