import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { AuthenticationService } from '../../Services/authentication/authentication.service';
import { DirectoryService } from '../../Services/directory/directory.service';
import { MatSnackBar } from '@angular/material/snack-bar';
import Drive from '../../Models/drive.model';
import Directory from '../../Models/directory.model';
import File from '../../Models/file.model';
import User from '../../Models/user.model';



@Component({
  selector: 'app-drive',
  templateUrl: './drive.component.html',
  styleUrls: ['./drive.component.css']
})
export class DriveComponent implements OnInit {

  path: string[] = []; 
  files: File[] = [];
  directories : Directory[] = [];
  directory : Drive = {};
  user : User = {};


  constructor(
    private routerService: Router,
    private authenticationService: AuthenticationService,
    private dirService : DirectoryService,
    private snackBar: MatSnackBar
    ) {}

  async ngOnInit(): Promise<void> {
    this.user = this.authenticationService.getUserInformation();
    await this.getDir(this.user.username +'/root');
    this.path.push('root');
  }




/**
   * Get Current path
   * @returns current path
   */
  public getCurrentPath(){
    let path = this.user.username + '/';
    this.path.forEach(segment => {
      path = path.concat(segment+'/');
    });
    return path;
  }


  /**
   * Change Dir to selected Dir
   * @returns void
   */
  public async onClickChangeDirForward(path:any){
    this.path.push(path);
    await this.getDir(this.getCurrentPath()+path);
    
  }

   /**
   * Change Dir to selected Dir
   * @returns void
   */
    public async onClickChangeDirBackward(path:any){
      let index = this.path.indexOf(path);
      this.path = this.path.slice(0,index+1);
      await this.getDir(this.getCurrentPath());
      
    }

  /**
   * Get dir from specific path
   * @returns void
   */
  public async getDir(path:string): Promise<void> {
    try {

      this.directory =  await this.dirService.getDir(path);
      this.directories = this.directory.directories as Directory[];
      this.files = this.directory.files as File[];
       

    } catch (err: any) {
      const { message } = err.error;
      this.snackBar.open(message, 'Close', {
        verticalPosition: 'top',
        duration: 3000,
      });
    }
  }
}

