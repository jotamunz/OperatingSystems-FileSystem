import { Component, OnInit } from '@angular/core';
import { DirectoryService } from '../../Services/directory/directory.service';

@Component({
  selector: 'app-create-directory',
  templateUrl: './create-directory.component.html',
  styleUrls: ['./create-directory.component.css'],
})
export class CreateDirectoryComponent implements OnInit {
  public directoryName: string = '';
  public isNameRepeated: boolean = false;

  constructor(private directoryService: DirectoryService) {}

  ngOnInit(): void {}

  public onSubmit(): void {
    return;
  }
}
