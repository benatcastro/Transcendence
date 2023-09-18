import { AuthService } from './auth.service';
import { Controller, Get, Query, Redirect, Req, Res } from '@nestjs/common';
import { log } from 'console';
import { Request, Response } from 'express';

@Controller('auth')
export class AuthController {
  constructor(private readonly AuthService: AuthService) {}

  @Get("login")
  redirectToIntraApi(@Req() req: Request, @Res() res: Response) {
    res.redirect(this.AuthService.getLoginRedirectURI());
  }

  @Get("api_response")
  postUserAuthorization(@Query() params: any) {
    
  }
}
