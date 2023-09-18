import { AuthService } from './auth.service';
import { Controller, Get, Redirect, Req, Res } from '@nestjs/common';
import { Request, Response } from 'express';

@Controller('auth')
export class AuthController {
  constructor(private readonly AuthService: AuthService) {}

  @Get("login")
  customRedirect(@Req() req: Request, @Res() res: Response) {
    res.redirect(this.AuthService.getLoginRedirectURI());
  }

  @Get("response")
  dothings(): string {
    return "hey im the response page";
  }
}

