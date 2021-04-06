import { Module, VuexModule, Mutation, Action } from 'vuex-module-decorators'
import Banco from '~/types/Banco'
import { $axios } from '~/utils/api'

@Module({
  name: 'bancos',
  stateFactory: true,
  namespaced: true,
})

class BancoModule extends VuexModule {
  bancosList: Banco[] = []

  @Mutation
  setBancos(bancos: Banco[]) {
    this.bancosList = bancos
  }

  @Action
  async getBancos() {
    const bancos = await $axios.$get('bancos/')
    this.setBancos(bancos)
  }

}

export default BancoModule
