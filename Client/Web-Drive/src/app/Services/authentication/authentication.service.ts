import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';

import User from '../../Models/user.model';
import { Observable } from 'rxjs';

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

  public authenticateUser(userData: User): Observable<Object> {
    return this.httpClient.post<Object>('/api/drives/login', userData);
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
