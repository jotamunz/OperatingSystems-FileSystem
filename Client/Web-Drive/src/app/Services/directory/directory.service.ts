import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { lastValueFrom } from 'rxjs';

import Directory from '../../Models/directory.model';


@Injectable({
  providedIn: 'root'
})
export class DirectoryService {

  constructor(private httpClient: HttpClient) { }

   /**
   * Retrieves from server directories data
   * @param path To the dir
   * @returns The response from the API
   */

 public getDir(path: string): Promise<any>{
  return lastValueFrom(this.httpClient.get('/api/dirs?dirPath='+path));
}
}

