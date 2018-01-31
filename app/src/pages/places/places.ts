import { Component } from '@angular/core';
import { NavController } from 'ionic-angular';


@Component({
  selector: 'page-places',
  templateUrl: 'places.html'
})
export class PlacesPage {

  constructor(public navCtrl: NavController) {

  }

  places = [
    {name:'moku', address:'moku-address', url:'moku-url'},
    {name:'Sooters', address:'Sooters-address', url:'Sooters-url'},
    {name:'Illusion', address:'Illusion-address', url:'Illusion-url'}
  ];

  itemSelected(item: string) {
    console.log("Selected Item", item);
  }

}



