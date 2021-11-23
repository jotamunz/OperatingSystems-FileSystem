import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-drive',
  templateUrl: './drive.component.html',
  styleUrls: ['./drive.component.css']
})
export class DriveComponent implements OnInit {
  path = ["Sistemas Operativos","Examenes"];
  files = [1,2,3,4,5,6];
  directories = [1,2,3];
  constructor() { }

  ngOnInit(): void {
  }

}
