import { Body, Controller } from "@nestjs/common";
import { Get, Post } from "@nestjs/common";
import { UserService } from "./user.service";
import { User } from "@prisma/client";

@Controller("user")
export class UserController {
  constructor(private readonly userService: UserService) {}

  @Post()
  async createUser(
    @Body() userData: { email: string; username: string; auth_type: string }
  ): Promise<User> {
    return await this.userService.create(userData);
  }

  @Get("all")
  async returnAll() {
    return await this.userService.all();
  }
}
