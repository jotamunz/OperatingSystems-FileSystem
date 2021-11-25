import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { lastValueFrom } from 'rxjs';

import File from '../../Models/file.model';

@Injectable({
  providedIn: 'root',
})
export class FileService {
  constructor(private httpClient: HttpClient) {}

  /**
   * Retrieves from server file data
   * @param path To the file
   * @returns The response from the API
   */
  public getFile(path: string, fileName: string): Promise<any> {
    return lastValueFrom(
      this.httpClient.get<any>(
        '/api/files?filePath=' +
          path +
          '&fileName=' +
          fileName +
          '&contentOnly=false'
      )
    );
  }

  /**
   * Creates a new file
   * @param fileData The data of the new file
   * @returns The information of the new file
   */
  public createFile(fileData: {
    filePath: string;
    extension: string;
    newFileName: string;
    content: string;
    forceOverwrite: boolean;
  }): Promise<any> {
    return lastValueFrom(this.httpClient.post<any>('/api/files', fileData));
  }
}
