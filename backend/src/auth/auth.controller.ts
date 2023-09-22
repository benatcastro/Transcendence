import { AuthService } from './auth.service';
import { Controller, Get, Query, Redirect, Req, Res } from '@nestjs/common';
import { AxiosError } from 'axios';
import { log } from 'console';
import { Request, Response } from 'express';
import { map } from 'rxjs';

@Controller('auth')
export class AuthController {
  constructor(private readonly AuthService: AuthService) {}

  @Get("login")
  redirectToIntraApi(@Req() req: Request, @Res() res: Response) {
    res.redirect(this.AuthService.getLoginRedirectURI());
  }

  @Get("api_response")
  async postUserAuthorization(@Query() params: any) {
      let access_token = await this.AuthService.PostUserAuth(params.code, params.state);
    

      log("access_token %s", access_token);
      return access_token;
    }
}
