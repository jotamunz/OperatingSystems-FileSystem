import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';

import Directory from 'src/app/Models/directory.model';

@Injectable({
  providedIn: 'root',
})
export class DirectoryService {
  private currentPath: string = '';

  constructor(private httpClient: HttpClient) {}

  /**
   * Adds a directory to the current path
   * @param directoryName The name of the directory to append
   */
  public addDirectoryToPath(directoryName: string): void {
    this.currentPath += `${directoryName}/`;
  }

  /**
   * Sets the current path to the root directory of the user
   */
  public setPathToRoot(): void {
    this.currentPath = this.currentPath.split('/')[0] + '/';
  }

  /**
   * Clears the current path
   */
  public clearPath(): void {
    this.currentPath = '';
  }

  public getCurrentPath(): string {
    return this.currentPath;
  }
}
