import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { AuthenticationService } from '../../Services/authentication/authentication.service';
import { DirectoryService } from '../../Services/directory/directory.service';
import { DriveService } from '../../Services/drive/drive.service';
import { MatSnackBar } from '@angular/material/snack-bar';
import Drive from '../../Models/drive.model';
import Directory from '../../Models/directory.model';
import File from '../../Models/file.model';
import User from '../../Models/user.model';
import Space from '../../Models/space.model';



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
  space : Space = {};



  constructor(
    private routerService: Router,
    private authenticationService: AuthenticationService,
    private dirService : DirectoryService,
    private driveService : DriveService,
    private snackBar: MatSnackBar
    ) {}

  async ngOnInit(): Promise<void> {
    this.user = this.authenticationService.getUserInformation();
    if(this.user.username != null){
      await this.getDir(this.user.username +'/root');
    this.path.push('root');
    this.getSpace(this.user.username);
    } 
  }



  /**
   * 
   * @returns used percentage
   */
 public getPercentageValue(usedSpace:any,totalSpace:any){
   let percenatage = (usedSpace*100)/totalSpace;

  return percenatage;
}

/**
   * Ends session
   * @returns void
   */
 public onClickLogout(){
  this.user.allocatedBytes = 0;
  this.user.password = '';
  this.user.username = '';
  this.authenticationService.setUserInformation(this.user);
  this.routerService.navigateByUrl('/');
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
   * Gets current space for the drive
   * @returns void
   */
 public async getSpace(username:string){
  if(this.user.username != null){
    this.space = await this.driveService.getDriveSpace(this.user.username);
  } 
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
   * Change Dir to selected Dir
   * @returns void
   */
    public async onClickChangeDir(path:any){
      this.path = [];
      this.path.push(path);
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

