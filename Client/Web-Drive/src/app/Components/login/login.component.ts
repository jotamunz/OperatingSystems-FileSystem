import { Component, OnInit } from '@angular/core';
import { FormControl, Validators } from '@angular/forms';
import { MatDialog } from '@angular/material/dialog';
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

  constructor(public dialog: MatDialog) {}

  ngOnInit(): void {}

  /**
   * Opens the signup dialog
   */
  public openDialog(): void {
    this.dialog.open(SignUpComponent);
  }
}
