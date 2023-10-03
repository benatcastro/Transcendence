import { Injectable } from '@nestjs/common';
import { PrismaService } from 'src/prisma/prisma.service';

@Injectable()
export class FriendService {
    constructor(private prisma: PrismaService) {}

  async findFriends(id: number) {
    return this.prisma.user.findUnique({
        where: { id: id },
        include: { friends: true }
    });
  }

  async addFriend(id: number, friendId: number) {


    return this.prisma.user.update({
        where: { id: id }, 
        data: {
            friends: {
              connect: {
                id: friendId,
              }
            }
        }
    })
  }

  async deleteFriend(id: number, friendId: number) {
    return this.prisma.user.update({
      where: { id: id },
      data: {
        friends: {
          disconnect: {
            id: friendId,
          }
        }
      }
    })
  }

}
