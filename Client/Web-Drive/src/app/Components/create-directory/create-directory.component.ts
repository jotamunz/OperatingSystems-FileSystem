import { Component, OnInit } from '@angular/core';
import { FormControl, Validators } from '@angular/forms';
import { DirectoryService } from '../../Services/directory/directory.service';
import { DriveService } from '../../Services/drive/drive.service';
import { AuthenticationService } from '../../Services/authentication/authentication.service';

@Component({
  selector: 'app-create-directory',
  templateUrl: './create-directory.component.html',
  styleUrls: ['./create-directory.component.css'],
})
export class CreateDirectoryComponent implements OnInit {
  public directoryName: string = '';
  public isNameRepeated: boolean = false;

  public directoryNameFormControl: FormControl = new FormControl('', [
    Validators.required,
  ]);

  constructor(
    private directoryService: DirectoryService,
    private driveService: DriveService,
    private authService: AuthenticationService
  ) {}

  ngOnInit(): void {}

  public async onSubmit(): Promise<void> {
    try {
      if (!this.directoryName) return;
      // Build request path
      const currentDirectoryPath = `${
        this.authService.getUserInformation().username
      }/${this.driveService.getCurrentPath().join('/')}`;
      const response = await this.directoryService.createDirectory(
        this.directoryName,
        currentDirectoryPath,
        false
      );
    } catch (error) {
      // Ask if directory should be overwritten
    }
  }
}
