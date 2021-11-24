import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';

import Drive from '../../Models/drive.model';
import { getLocaleDirection } from '@angular/common';
import { lastValueFrom } from 'rxjs';


@Injectable({
  providedIn: 'root'
})
export class DirectoryService {

  constructor(private httpClient: HttpClient) { }

   /**
   * Retrieves from server directories data
   * @param dirData The retrieved info
   * @returns The response from the API
   */

 public getDir(path: string): Promise<any>{
  return lastValueFrom(this.httpClient.get('/api/dirs?dirPath='+path));
}
}

