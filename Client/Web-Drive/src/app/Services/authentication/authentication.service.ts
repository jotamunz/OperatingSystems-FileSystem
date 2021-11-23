import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';

import User from '../../Models/user.model';
import { catchError, lastValueFrom, Observable, of } from 'rxjs';

@Injectable({
  providedIn: 'root',
})
export class AuthenticationService {
  private userInformation: User = {
    username: '',
    allocatedBytes: undefined,
  };
  private isAuthenticated: boolean = false;

  constructor(private httpClient: HttpClient) {}

  /**
   * Authenticates user with credentials
   * @param userData The credentials of the user
   * @returns The response from the API
   */
  public authenticateUser(userData: User): Promise<any> {
    return lastValueFrom(this.httpClient.post('/api/drives/login', userData));
  }

  public getUserInformation(): User {
    return this.userInformation;
  }

  public getIsAuthenticated(): boolean {
    return this.isAuthenticated;
  }

  public setIsAuthenticated(isAuthenticated: boolean): void {
    this.isAuthenticated = isAuthenticated;
  }

  public setUserInformation(user: User): void {
    this.userInformation = user;
  }
}
