import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { lastValueFrom } from 'rxjs';

import User from '../../Models/user.model';

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

  /**
   * Registers a new user with its own Drive
   * @param userData The data of the user
   * @returns The data of the new user
   */
  public registerUser(userData: any): Promise<User> {
    return lastValueFrom(this.httpClient.post('/api/drives', userData));
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
