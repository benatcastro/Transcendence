import { AuthService } from './auth.service';
import { Controller, Get, Query, Redirect, Req, Res } from '@nestjs/common';
import { AxiosError } from 'axios';
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
    log("params.code: " + params.code);
    try {
      this.AuthService.PostUserAuth(params.code, params.state);
    } catch (error: any) {
     log(error) ;
    }
  }
}
