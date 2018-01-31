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
    {id:1, name:'moku', address:'moku-address', url:'moku-url'},
    {id:2, name:'Sooters', address:'Sooters-address', url:'Sooters-url'},
    {id:3, name:'Illusion', address:'Illusion-address', url:'Illusion-url'}
  ];

  itemSelected(id: number) {
    console.log("Selected Item id is", id);
  }

}



