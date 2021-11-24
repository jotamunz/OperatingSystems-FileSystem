import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { lastValueFrom } from 'rxjs';

import Drive from '../../Models/drive.model';


@Injectable({
  providedIn: 'root'
})
export class DriveService {

  constructor(private httpClient: HttpClient) { }


     /**
   * Retrieves from server directories data
   * @param dirData The retrieved info
   * @returns The response from the API
   */

 public getDriveSpace(username: string): Promise<any>{
  return lastValueFrom(this.httpClient.get('/api/drives/spaces?username='+username));
}
}
