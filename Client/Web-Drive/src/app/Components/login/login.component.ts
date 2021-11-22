import { Component, OnInit } from '@angular/core';
import { FormControl, Validators } from '@angular/forms';
import { MatDialog } from '@angular/material/dialog';
import { AuthenticationService } from '../../Services/authentication/authentication.service';
import { SignUpComponent } from '../sign-up/sign-up.component';

import User from '../../Models/user.model';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css'],
})
export class LoginComponent implements OnInit {
  public user: User = {
    username: '',
    password: '',
  };

  public loginFormControl: FormControl = new FormControl('', [
    Validators.required,
  ]);
  public passwordFormControl: FormControl = new FormControl('', [
    Validators.required,
  ]);

  constructor(
    private dialog: MatDialog,
    private authenticationService: AuthenticationService
  ) {}

  ngOnInit(): void {}

  /**
   * Opens the signup dialog
   */
  public openDialog(): void {
    this.dialog.open(SignUpComponent);
  }

  /**
   * Authenticates user with entered credentials
   * @returns void
   */
  public onSignInClick(): void {
    if (!this.user.username || !this.user.password) {
      return;
    }
    this.authenticationService
      .authenticateUser(this.user)
      .subscribe((response: Object) => {
        console.log(response);
      });
  }
}
