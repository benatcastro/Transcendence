import { Body, Controller, NotFoundException, Param, Query } from '@nestjs/common';
import { Get, Post, Delete, Put } from '@nestjs/common';
import { UserService } from './user.service';
import { User } from '@prisma/client';
import { log } from 'console';

@Controller('user')
export class UserController {
    constructor(private readonly userService: UserService) {}

  @Post()
    async createUser(
    @Body() userData: { email: string; username: string; auth_type: string },
    ): Promise<User> {
        const users = await this.userService.create(userData);
        if (!users)
          throw new NotFoundException(`No users found`);

        return users;
    }

  @Get()
  async returnAll() {
      return await this.userService.all();
  }

  @Get(':id')
  async getUserById(@Param('id') id: string) {
    log("entra");
      const user = await this.userService.findById(Number(id));

    if (!user)
      throw new NotFoundException(`User with id: ${id} does not exist.`);
    return user;
  }
  
  @Get(':id/friend')
  async getFriends(@Param('id') id: string) {
    return await this.userService.findFriends(Number(id));

  }

  @Post(':id/friend')
  async addFriend(@Param('id') id: string, @Body('friendId') friendId: string) {
    log(id);
    log(friendId);
    const result = await this.userService.addFriend(Number(id), Number(friendId));
  }

  @Put('email/:id')
  async updateEmail(@Param('id') id: string, @Body() email: string) {
    const update = await this.userService.updateEmail(Number(id), email);
    return update;
  }

  @Put(':id')
  async generalUpdate(@Param('id') id: number, @Body() userData: { email: string, username: string, auth_type: string }) {
    const update = await this.userService.updateUser(Number(id), userData);
    return update;
  }

  @Put('username/:id')
  async updateUsername(@Param('id') id: string, @Body() username: string) {
    const update = await this.userService.updateUsername(Number(id), username)
    return update;
  }

}
